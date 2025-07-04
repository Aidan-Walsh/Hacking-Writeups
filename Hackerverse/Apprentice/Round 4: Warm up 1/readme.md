- This involves finding the password to the given file c1.jar
- First we need to unzip this .jar file by using the command: ```jar -xf c1.jar```
- This then gives us the file "a.class"
- When using the command ``` file a.class``` we see that it is a compiled java executable that asks for a password
- We can use an online java decompiler to further inspect this. Refer to the file a.java to follow along.
- There is a fair amount of code to look through, but after looking at main(), we see that i() is used to determine whether we are granted access or not.
- i() uses 3 functions (m,n,o). Functions m and n are complicated and allow many different combinations to pass, and are designed to keep us solely focused on them.
- Function o, however, only has one input that passes.
- O just iterates over the input and xors each character with the value of u() and tests equivalence with an array of values.
- Due to the associativity of xor, we can reverse this function in java to solve for the password that we need. The snippet below shows this code
-  <img width="689" alt="Screenshot 2025-06-30 at 3 18 26 PM" src="https://github.com/user-attachments/assets/503d02aa-4b67-4987-ba8a-a6a8b2520064" />
- When we run this code, we get the following output: 
- <img width="262" alt="Screenshot 2025-06-30 at 3 19 08 PM" src="https://github.com/user-attachments/assets/dd0bd0e3-ef95-495e-8533-a9c0baffbf0b" />
