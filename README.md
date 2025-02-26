# Login API
API đăng nhập đơn giản sử dụng Flask, SQLite và JWT.

## Cài đặt
1. Tạo môi trường ảo: `python -m venv venv`
2. Kích hoạt: `venv\Scripts\activate` (Windows) hoặc `source venv/bin/activate` (Mac/Linux)
3. Cài đặt thư viện: `pip install -r requirements.txt`
4. Chạy app: `python run.py`

## API Endpoint
- **POST /login**
  - Body: `{"username": "testuser", "password": "testpass"}`
  - Response thành công: `{"message": "Login successful", "token": "<JWT_TOKEN>"}`