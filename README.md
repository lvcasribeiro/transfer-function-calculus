## Transfer Functions Calculus

This code aims to analyze any second-order control system and transfer functions in a practical way, using the python programming language and having as main reference the **control** library, in addition to other libraries that are fundamental for any math analysis, like **numpy** and **matplotlib**. In this way, it is possible to practically perform the main analyzes of the system and have a basic idea of what's happening with the system.

##

### Important information

Initially, the user can choose to perform the analysis using two methods: 

###### First method:
The first method allows the user to start the study of the system using the ready transfer function:
```python
create_transfer_function_system();
```

<br>

###### Second method:
The second one allows entering the state equations (state, input and output matrixes) to create the transfer function:
```python
create_state_equations_system();
```

##

### Starting with the script

Once the functions have been created, it is possible to perform the following analyzes of this second-order system:

###### 1. Instantiate the class:
```python
control = Transfer_Function_Control();
```

<br>

###### 2. Input your system, in this case, using the first method:
```python
control.create_transfer_function_system();
```

```
How many coefficients does the numerator have? 2
How many coefficients does the denominator have? 3

For orders where the coefficients are zero, enter: 0.

Enter the numerator coefficients in the correct order: 1
Enter the numerator coefficients in the correct order: 1

Enter the denominator coefficients in the correct order: 1
Enter the denominator coefficients in the correct order: 4
Enter the denominator coefficients in the correct order: 2

System obtained through the transfer function: 
 
    s + 1
-------------
s^2 + 4 s + 2
```

<br>

###### 3. Calling the function to see the system behavior graph as a natural response:
```python
control.isolated_analysis();
```

![first-image](https://user-images.githubusercontent.com/96185134/193414464-a442ca0f-cd9d-4a36-a19c-f3cbff8fd7f0.jpg)

<br>

###### 4. Apply a feedback to the natural response:
```python
control.simple_feedback();
```

![second-image](https://user-images.githubusercontent.com/96185134/193414477-84bbe12b-a1c3-4d72-997d-b53f08f3cd12.jpg)

<br>

###### 5. Create another system to the natural response to make the control, in this case a step input:
```python
control.system_of_control();
```

```
How many coefficients does the numerator have? 1
How many coefficients does the denominator have? 2

For orders where the coefficients are zero, enter: 0.

Enter, in the correct order, the coefficients of the numerator: 1

Enter, in the correct order, the coefficients of the denominator: 1
Enter, in the correct order, the coefficients of the denominator: 0

1
-
s
```

<br>

###### 6. Calling the function to see the system behavior graph as a natural response with the new system:
```python
control.in_series();
```

![third-image](https://user-images.githubusercontent.com/96185134/193414488-c88514af-cc18-4b5e-b784-ceb8257671c8.jpg)

<br>

###### 7. Apply a feedback to the natural response with the new system:
```python
control.in_series_with_feedback();
```

![fourth-image](https://user-images.githubusercontent.com/96185134/193414502-2a7a3ee8-6669-4592-8094-2dc7a80984df.jpg)
