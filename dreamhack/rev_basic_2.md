# Reversing Basic Challenge #2

Let's open the program with IDA

![main_func](https://i.ibb.co/BMkNK8p/Screenshot-2025-12-27-164150.png)

We can see ```test eax, eax```, which performs an AND operation between eax and itself. If eax is 1, the zero flag will be set to 0 and ```jz short loc_7FF7B6721186``` will print out **"Correct"**.

Function sub_7FF7B6721000 is called after our input, let's look inside it.

![sub_func](https://i.ibb.co/MxGw67ms/Screenshot-2025-12-27-165148.png)

## Block 1
```
mov     [rsp+arg_0], rcx
sub     rsp, 18h
mov     [rsp+18h+var_18], 0
jmp     short loc_7FF7B672101A
```
[rsp+arg_0] hold our input value, which is 8 bytes higher than current stack pointer.
Then rsp went down 18 bytes, these 18 bytes are used to hold the loop counter, as we can see in the 3rd line.

## Block 2
```
movsxd  rax, [rsp+18h+var_18]
cmp     rax, 12h
jnb     short loc_7FF7B6721048
```

From now on let's call [rsp+18h+var18] i, which is our loop counter.
Block 2 compares i with 12h, which is 1*16+2=18 bytes.
If i reaches 18, the program will stop the loop and jump.
## Block 3
```
movsxd  rax, [rsp+18h+var_18]
lea     rcx, aC         ; "C"
movsxd  rdx, [rsp+18h+var_18]
mov     r8, [rsp+18h+arg_0]
movzx   edx, byte ptr [r8+rdx]
cmp     [rcx+rax*4], edx
jz      short loc_7FF7B6721046
```
rax, rdx holds value of i, rcx holds the pointer to where 'C' is stored. the 'C' here is the first char of our secret array, which is the correct input.

r8 holds the start address of our input.

```movzx edx, byte ptr [r8+rdx]```: edx holds the ith char of our input, ```byte ptr``` means grabbing 1 byte.

```cmp [rcx+rax*4], edx```: performs a subtraction of [rcx+rax*4] and edx, basically compares 2 value.

![data_section](https://i.ibb.co/Ndx9rG1X/Screenshot-2025-12-27-173339.png)

Looking at our data section, we can see the address of each char of the array are 4 bytes apart.

```align 4``` means moving to the nearest higher address that is divisible by 4.

| Address   | Char |              |
| -------   | ---- | ------------ |
| 0x...3000 | C    |start address |
| 0x...3004 | o    |divisible by 4|
| 0x...3008 | m    |divisible by 8|

Therefore, [rcx+rax*4] holds the ith char of the secret array.
if 2 values are equal, the subtraction will be 0 and zero flag will be set to 1.

The jz will jump to block 7, which increase i by 1 and go back to block 2.

## Solution
Looking at the data section again, we will be able to achieve the secret array: **Comp4re_the_arr4y**

The flag is **DH{Comp4re_the_arr4y}**
