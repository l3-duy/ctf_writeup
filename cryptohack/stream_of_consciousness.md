# Stream Of Consciousness

Đầu tiên ta sẽ tìm một số ciphertext bằng cách request nhiều lần:

```python
url='https://aes.cryptohack.org/stream_consciousness/encrypt/'
for i in range(32):
    response=requests.get(url).json()
    res=bytes.fromhex(response['ciphertext'])
    if res not in cipher_list:
        cipher_list.append(res)
```

Bởi các text đều dùng chung một keystream, và ta đã biết ```keystream = ciphertext XOR plaintext```, ta sẽ tìm ciphertext của flag bằng cách duyệt qua ```cipher_list``` và kiểm tra xem keystream nào hợp lệ.

keystream sẽ hợp lệ nếu mọi plaintext trả về chỉ chứa printable chars.

![finding_ks](https://i.ibb.co/0yKfMvtN/soc-1.png)

![](https://i.ibb.co/Wv0shFvg/soc-2.png)

Ta có được keystream và một phần của các text ban đầu:

![result](https://i.ibb.co/TxSLjvRT/soc-3.png)

Từ các text ban đầu, ta dễ dàng dự đoán các kí tự tiếp theo của chúng, từ đó tìm được các kí tự tiếp theo của ```flag```.

Ví dụ với text 3, kí tự tiếp theo có thể là "l".

![finding_flag](https://i.ibb.co/mVbQjp1h/soc-4.png)

Tiếp tục thử nhiều lần, ta sẽ tìm được flag.

Kết quả: **crypto{k3y57r34m_r3u53_15_f474l}**

