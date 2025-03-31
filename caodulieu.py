import os
import requests
from bs4 import BeautifulSoup

# URL trang cần cào dữ liệu
URL = "https://www.vinmec.com/vie/bai-viet/nguyen-nhan-benh-u-lympho-ac-tinh-khong-hodgkin-vi"

# Thư mục lưu dữ liệu
SAVE_DIR = "D:/ChatBotThucTap/demo/data_in"
os.makedirs(SAVE_DIR, exist_ok=True)

# Tên file TXT để lưu nội dung
FILENAME = os.path.join(SAVE_DIR, "u_lympho_ac_tinh.txt")

def scrape_and_save(url, filename):
    """Cào dữ liệu từ trang web và lưu vào file TXT kèm link bài viết"""
    try:
        # Gửi yêu cầu HTTP đến trang web
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Kiểm tra lỗi HTTP

        # Phân tích HTML bằng BeautifulSoup
        soup = BeautifulSoup(response.text, "lxml")

        # Lấy nội dung từ thẻ chứa bài viết
        paragraphs = soup.find_all("p")  # Nếu trang web dùng thẻ khác, cần điều chỉnh

        # Trích xuất nội dung và nối lại thành văn bản
        content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])

        if not content:
            raise ValueError("Không tìm thấy nội dung bài viết!")

        # Thêm link bài viết vào nội dung
        full_content = f"🔗 Link bài viết: {url}\n\n{content}"

        # Lưu nội dung vào file TXT
        with open(filename, "w", encoding="utf-8") as file:
            file.write(full_content)

        print(f"✅ Đã lưu dữ liệu vào {filename}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi khi tải trang web: {e}")
    except Exception as e:
        print(f"❌ Lỗi khi xử lý dữ liệu: {e}")

# Chạy cào dữ liệu
scrape_and_save(URL, FILENAME)