# Bài tập đánh giá Trainee AI/Automation - Kyanon Digital (Câu 2)

Đây là mã nguồn cho bài tập kỹ thuật (mini workflow) của Kyanon Digital.

## Mô tả

Chương trình `process_emails.py` (viết bằng Python) thực hiện các nhiệm vụ:
* Đọc dữ liệu từ file `emails.csv`.
* Lọc tất cả các email có liên quan đến "leave request" bằng cách tìm từ khóa "leave" trong `subject` hoặc `body`.
* Xuất kết quả lọc ra file `leave_request.json` với cấu trúc được yêu cầu.

## Cách chạy

1.  Clone repository này.
2.  Đảm bảo bạn đã cài đặt Python 3.
3.  Chạy lệnh sau từ terminal:
    ```bash
    python3 process_emails.py
    ```
4. Có thể thay đổi input file là `emails.csv`.
5. Kết quả sẽ được lưu trong file `leave_request.json`.