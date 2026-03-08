# very cool native app

Đổi định dạng thành *chals.zip*, tiến hành giải nén
![](https://i.ibb.co/MxHnqkD1/image.png)

Nhận thấy app được chạy bàng hermes, ta dịch ngược file *main.jsbundle* bằng công cụ hermes-dec
(https://github.com/P1sec/hermes-dec)

Mở file JS đã dịch ngược, thử search các xâu quen thuộc như "BKSEC", ta thấy
![](https://i.ibb.co/FkRxCc8J/image.png)

Khả năng cao đây sẽ là 1 phần của flag hoàn chỉnh

Lướt xuống một chút, ta thấy rất nhiều các thao tác tính toán và so sánh char được thực hiện ở hàm _w9p:
![](https://i.ibb.co/GQX5fzpz/image.png)

Phần đầu của flag ta tìm được trước đó ("BKSEC{just_some_mobiel_thing_") chứa 29 kí tự, và hàm _w9p lấy các char bắt đầu từ index 29 (kí tự 30), nên đây sẽ là phần còn lại của flag

Copy lại và gửi cho AI, ta được phần còn lại: "60427954_32__385_8__66_42098417_"
![](https://i.ibb.co/8DwQChkD/image.png)
![](https://i.ibb.co/99m3GTj5/image.png)
Kết hợp với part đầu ta có flag hoàn chỉnh: 
**BKSEC{just_some_mobiel_thing_60427954f32bb385c8ee66f42098417f}**