from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request, HTTPException, Form, Response, status, Path
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, HttpUrl

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
import os

# --- SQLAlchemy Database Setup ---
SQLITE_DB_URL = "sqlite:///./users.db"
engine = create_engine(SQLITE_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    profile_picture_url = Column(String, nullable=True)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- FastAPI App Setup (with Lifespan) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting up...")
    create_tables()
    db = next(get_db())
    if not db.query(User).filter(User.username == "admin").first():
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_context.hash("password123")
        db.add(User(username="admin", hashed_password=hashed_password, is_admin=True, profile_picture_url="https://via.placeholder.com/150?text=Admin"))
        db.commit()
    db.close()
    yield
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")

# --- Security Configuration ---
SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "your-super-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- Auth Dependencies ---
def get_current_user_for_html(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, headers={"Location": "/"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username: raise HTTPException(status_code=401)
        user = db.query(User).filter(User.username == username).first()
        if not user: raise HTTPException(status_code=401)
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, headers={"Location": "/"})

def get_current_user_for_api(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token: raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username: raise HTTPException(status_code=401, detail="Invalid token payload")
        user = db.query(User).filter(User.username == username).first()
        if not user: raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_admin(current_user: User = Depends(get_current_user_for_api)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not an admin")
    return current_user

# --- Pydantic Models for API ---
class UserIn(BaseModel):
    username: str
    password: str
    is_admin: bool = False
    profile_picture_url: HttpUrl | None = None

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    is_admin: bool | None = None
    profile_picture_url: HttpUrl | str | None = None

# --- Routes ---

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/token")
async def login_for_access_token(response: Response, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    response.set_cookie(key="access_token", value=access_token, httponly=True, samesite="strict")
    return {"message": "Login successful", "is_admin": user.is_admin}

@app.post("/api/logout")
async def api_logout(response: Response, current_user: User = Depends(get_current_user_for_api)):
    response.delete_cookie(key="access_token")
    return JSONResponse(content={"message": "Logged out successfully"}, status_code=200)

@app.get("/authorized/{filepath:path}", response_class=HTMLResponse)
async def serve_authorized_page(request: Request, filepath: str, current_user: User = Depends(get_current_user_for_html)):
    file_path = os.path.join("templates", "authorized", filepath)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Page not found")
    
    return templates.TemplateResponse(f"authorized/{filepath}", {"request": request, "user": current_user})

# --- User API Endpoints ---
@app.get("/api/me")
async def get_my_data(current_user: User = Depends(get_current_user_for_api)):
    return {
        "username": current_user.username,
        "is_admin": current_user.is_admin,
        "profile_picture_url": current_user.profile_picture_url
    }

# --- Admin API Endpoints ---
@app.get("/api/admin/users")
async def get_all_users(db: Session = Depends(get_db), admin_user: User = Depends(get_current_admin)):
    users = db.query(User).all()
    return [{"id": u.id, "username": u.username, "is_admin": u.is_admin, "profile_picture_url": u.profile_picture_url} for u in users]

@app.post("/api/admin/users")
async def create_new_user(user_in: UserIn, db: Session = Depends(get_db), admin_user: User = Depends(get_current_admin)):
    existing_user = db.query(User).filter(User.username == user_in.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = get_password_hash(user_in.password)
    # Corrected: Convert HttpUrl to string before saving
    profile_pic_url_str = str(user_in.profile_picture_url) if user_in.profile_picture_url else None
    
    new_user = User(username=user_in.username, hashed_password=hashed_password, is_admin=user_in.is_admin, profile_picture_url=profile_pic_url_str)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

@app.delete("/api/admin/users/{user_id}")
async def delete_user(user_id: int = Path(..., gt=0), db: Session = Depends(get_db), admin_user: User = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.id == admin_user.id:
        raise HTTPException(status_code=403, detail="Cannot delete your own account")
        
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

@app.put("/api/admin/users/{user_id}")
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db), admin_user: User = Depends(get_current_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id == admin_user.id and user_update.is_admin is not None and not user_update.is_admin:
        raise HTTPException(status_code=403, detail="Cannot remove your own admin status")

    if user_update.username is not None:
        user.username = user_update.username
    if user_update.password is not None:
        user.hashed_password = get_password_hash(user_update.password)
    if user_update.is_admin is not None:
        user.is_admin = user_update.is_admin
    # Corrected: Convert HttpUrl to string before saving
    if user_update.profile_picture_url is not None:
        user.profile_picture_url = str(user_update.profile_picture_url)
    
    db.commit()
    db.refresh(user)
    return {"message": "User updated successfully"}

# This is the code that makes it run when you execute "python main.py"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)