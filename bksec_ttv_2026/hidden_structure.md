# Hidden Structure

Nhận thấy p và q không độc lập mà phụ thuộc vào x và y, ta nghĩ tới việc tìm x và y trước.

$$ N = (x * B + y)*(y * B + x ) $$

$$N = xy * B^2 + (x^2 + y^2)B + xy$$

Đặt $P=x*y$, $S=x^2+y^2$

$$ => N = P * B^2 + S * B + P$$

Vì $P=x * y$ nên $\approx 512$ bit, ta có thể viết $P$ dưới dạng $k * B+N_0$, với $B=2^{256}$

$$N = (k * B + N_0)B^2 + S * B + (k * B + N_0)$$

$$N = k * B^3 + N_0 * B^2 + (S + k)B + N_0 \tag{1}$$

$$ => N_0 = N \pmod B$$

Tìm được $N_0$, thế vào (1):

$$ => M = \frac{N - N_0 * B^2 - N_0}{B} = k * B^2 + S + k$$

Chia hai vế cho $B^2$, nhận thấy $\frac{S}{B^2} + \frac{k}{B^2} < \frac{2*B^2}{B^2} + \frac{k}{B^2} < 3$, dự đoán được k, từ đó xây dựng x,y theo P,S

```python
import math
from Crypto.Util.number import long_to_bytes, inverse
N = 107444638859099155759777187090231262569833054720517547475456101236477286061642951211232522980016935214117151901316067288134076019258357378153815894696105422994651894516549086845637403949534145390050746353299397783409065996987527927026314423191436300386280922075865669873754956335784354470237039709346406222789
e = 65537
c = 56143710973900761339774002971192037727375234874650436422245945684342980716505499471085786012340621409106405319356586450688993792522513823502401085339774194961300841598824881056390845294225756335102709315028822707701848497421372062559501439381841852116763699839771135406441292657937478625029095325072727620068
B = 1 << 256
N0 = N % B
M = (N - N0 * B**2 - N0) // B
k_est = M // (B**2)
for k in range(k_est-3 , k_est):
    P = k * B + N0
    S = M - k * B**2 - k
    if S < 0:
        continue
    tongbp = S + 2 * P # (x+y)^2
    hieubp = S - 2 * P # (x-y)^2
    if tongbp >= 0 and hieubp >= 0:
        tong = math.isqrt(tongbp)
        hieu = math.isqrt(hieubp)
        if tong**2 == tongbp and hieu**2 == hieubp:
            x = (tong + hieu) // 2
            y = (tong - hieu) // 2
            p = x * B + y
            q = y * B + x
            if p * q == N:
                phi = (p-1)*(q-1)
                d = inverse(e, phi)
                m = pow(c, d, N)
                print(long_to_bytes(m).decode())
                break
```
Flag: **BKSEC{p4l1n_p0ly_1d3n717y_m47h}**

