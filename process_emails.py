import csv
import json

def filter_leave_requests(input_file, output_file):
    """
    Đọc file CSV, lọc các email xin nghỉ phép và xuất ra file JSON.
    """
    leave_requests = []
    keyword = "leave"

    try:
        with open(input_file, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            for row in reader:
                subject_lower = row.get('subject', '').lower()
                body_lower = row.get('body', '').lower()
                
                # Lọc email dựa trên từ khóa
                if keyword in subject_lower or keyword in body_lower:
                    # Tạo đối tượng mới theo cấu trúc yêu cầu
                    request_data = {
                        "id": int(row['id']), 
                        "sender": row['sender'],
                        "type": "leave_request"
                    }
                    leave_requests.append(request_data)
        
        # Ghi kết quả ra file JSON
        with open(output_file, mode='w', encoding='utf-8') as outfile:
            json.dump(leave_requests, outfile, indent=2) # indent=2 giúp file JSON đẹp và dễ đọc hơn
            
        print(f"✅ Xử lý thành công! Kết quả đã được lưu tại: {output_file}")

    except FileNotFoundError:
        print(f"❌ Lỗi: Không tìm thấy file {input_file}")
    except Exception as e:
        print(f"❌ Đã xảy ra lỗi: {e}")

# Chạy hàm chính
if __name__ == "__main__":
    filter_leave_requests('emails.csv', 'leave_request.json')