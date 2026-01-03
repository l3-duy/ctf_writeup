# Dancing Queen

```
flag_enc = c.encrypt(FLAG, key, iv2)
```

Biết được ```flag_enc``` và ```iv2```, để lấy được ```FLAG``` ta có thể tìm ```key``` bằng cách dịch ngược công đoạn mã hóa.

![reverse](https://i.ibb.co/v4cwTphr/dq-1.png)

![enc_func](https://i.ibb.co/kVZzvnw7/dq-3.png)

Để tìm được ```key```, ta chỉ cần xét vòng lặp đầu, ứng với 64 byte đầu tiên của ```m```
```
state=bytes_to_words(xor(msg,msg_enc)[:64])
for i in range(10):
    reverse_inner_block(state)
key=words_to_bytes(state[4:])[:32]
```
Sau đó decrypt lại ```flag_enc``` để trả về ```FLAG```
```
FLAG=c.decrypt(flag_enc, key, iv2)
```
Kết quả:
**crypto{M1x1n6_r0und5_4r3_1nv3r71bl3!}**


