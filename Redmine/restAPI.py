import requests
from requests.auth import HTTPBasicAuth

# Thông tin kết nối tới Redmine
redmine_url = "http://localhost:3000"  # Thay đổi URL của Redmine
api_key = "012dd5d50fddb99e1f2cecc48262e46150fe0bd9"  # Thay đổi với API Key của bạn
project_id = "2"  # Thay đổi với ID của project bạn muốn tạo issue

# Dữ liệu issue cần tạo
issue_data = {
    "issue": {
        "project_id": project_id,
        "subject": "Bug #123 - Khong the dang nhap",
        "description": "Nguoi dung bao loi khi nhap mat khau dung nhung khong the dang nhap",
        "status_id": 5,  # Trạng thái "Mới"
        "priority_id": 1,  # Ưu tiên "Cao"
        "assigned_to_id": 8  # ID của lập trình viên A (có thể lấy từ quản trị viên của bạn)
    }
}

# Gửi yêu cầu tạo issue
response = requests.post(
    f"{redmine_url}/issues.json",
    json=issue_data,
    auth=HTTPBasicAuth(api_key, "x")
)

# Kiểm tra kết quả
if response.status_code == 201:
    print("Issue đã được tạo thành công!")
else:
    print(f"Lỗi khi tạo issue: {response.status_code}")
    print(response.text)
