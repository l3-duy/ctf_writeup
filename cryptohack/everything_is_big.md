# Everything Is Big

Bởi số d nhỏ (256 bit), ta có thể dùng phương pháp Wiener attack để tìm được d.

Từ $d \equiv e^{-1} \pmod{\phi(n)}$ ta có:

$$ed - k\phi(n) = 1$$

Chia hai vế cho $d\phi(n)$

$$\left| \frac{e}{\phi(n)} - \frac{k}{d} \right| = \frac{1}{d\phi(n)}$$

Với $k<d<\frac{1}{3}n^\frac{1}{4}$, $\phi(n) \approx n$, $p \approx \sqrt{n}$, $q \approx \sqrt(n)$, $n=pq$, $\phi(n)=(p-1)(q-1)$, ta có:

$$\left| \frac{e}{\phi(n)} - \frac{k}{d} \right| = \left| \frac{e}{n} - \frac{k}{d} \right| = \left| \frac{ed-k\phi(n)-kn+k\phi(n)}{nd} \right| = \left| \frac{1-k(p+q-1)}{nd} \right| \approx \left| \frac{1-k(2\sqrt{n}-1)}{nd} \right| < \frac{3k}{d\sqrt{n}} < \frac{1}{2d^2}$$ 

Áp dụng dãy hội tụ liên phân số:

![get_convergents](https://i.ibb.co/kkGhJHG/eisb-1.png)

Sau đó, thử từng ```d``` với một msg bất kì và kiểm tra xem có msg gốc có được trả lại không.

![](https://i.ibb.co/4RGXC2kp/eisb-3.png)

Kết quả: **crypto{s0m3th1ng5_c4n_b3_t00_b1g}**