# Importing libraries:
from control.matlab import *

import matplotlib.pyplot as pypt
import control as pyct
import numpy as pynp
import time as pytm

import warnings

%matplotlib inline

# Turning off the warnings:
warnings.filterwarnings('ignore');

# Class of transfer functions calculus:
class Transfer_Function_Control():
    # Constructor:
    def __init__(self):
        self.state_variables = 0;
        self.control_system = 0;
        self.feedback = 0;
        self.system = 0;
        self.series = 0;
        self.K = 0;

        self.A = 0;
        self.B = 0;
        self.C = 0;

    # Creating the main system with the transfer function:
    def create_transfer_function_system(self):
        numerator = [];
        denominator = [];
        
        quantity_of_numerators = int(input("How many coefficients does the numerator have? "));
        quantity_of_denominators = int(input("How many coefficients does the denominator have? "));
        
        print("\nFor orders where the coefficients are zero, enter: 0.\n");
        
        for i in range(0, quantity_of_numerators):
            i = float(input("Enter the numerator coefficients in the correct order: "));
            numerator.append(i);

        numerator = pynp.array(numerator);
        print('');

        for j in range(0, quantity_of_denominators):
            j = float(input("Enter the denominator coefficients in the correct order: "));
            denominator.append(j);

        denominator = pynp.array(denominator);

        self.system = pyct.tf([[numerator]], [[denominator]]);

        print(f'\nSystem obtained through the transfer function: \n {self.system}');

    # Create system from the equations of state:
    def create_state_equations_system(self):
        # Create the state matrix. Respect the input order according to the reference matrix:
        self.state_variables = int(input("How many state variables? "));
        print('');

        # State matrix A:
        list_A = [];
        for i in range(0, int(self.state_variables*self.state_variables)):
            i = int(input("Enter in the correct order the values of the state matrix: "));
            list_A.append(i);

        self.A = pynp.array(list_A, dtype = float);
        self.A.resize(self.state_variables, self.state_variables);
        self.A = self.A.tolist();

        print(f'\nState matrix: \n {self.A}\n');

        # State matrix B:
        list_B = [];
        for j in range(0, int(self.state_variables)):
            j = int(input("Enter in the correct order the values of the input matrix: "));
            list_B.append(j);

        self.B = pynp.array(list_B, dtype = float);
        self.B.resize(self.state_variables, 1);
        self.B = self.B.tolist();

        print(f'\nInput matrix: \n {self.B}\n');

        # State matrix C:
        list_C = [];
        for k in range(0,int(self.state_variables)):
            k = int(input("Enter in the correct order the values of the output matrix: "));
            list_C.append(k);

        self.C = pynp.array(list_C, dtype = float);
        self.C.resize(1, self.state_variables);
        self.C = self.C.tolist();

        print(f'\nOutput matrix: \n {self.C}\n');

        self.system = StateSpace(self.A, self.B, self.C, 0);
        print(self.system);

        self.system = pyct.tf(self.system);
        print(f'\nSystem obtained through the state equations: \n {self.system}');
    
    # Method for graphical analysis of the natural response:
    def isolated_analysis(self):    
        print("Transfer function plot: \n");
        pytm.sleep(0.5);
        pypt.figure(1);

        fig, natural_response_transfer_function = pypt.subplots();
        yout, T = impulse(self.system);
        pypt.plot(T.T, yout.T);

        natural_response_transfer_function.set_title("Natural Response");
        natural_response_transfer_function.set_ylabel('Voltage [V]');
        natural_response_transfer_function.set_xlabel('Time [s]');

        pypt.show(block = False);
        pytm.sleep(0.5);
        
        # Poles and zeros:
        # print("Poles and zeros: \n");
        # damp(self.system);
        # pzmap(self.system);

        pytm.sleep(0.5);
        
        # Root-Locus:
        print("Root-Locus: \n");
        pytm.sleep(0.5);
        rlocus(self.system);
    
    # Feedback to the natural response:
    def simple_feedback(self):
        self.feedback = pyct.feedback(self.system, sys2 = 1, sign = 1);
        print("Transfer function with feedback: \n");
        print(self.feedback);
        pytm.sleep(0.5);

        print("Feedback plot: \n")
        pytm.sleep(0.5);
        pypt.figure(2);
        fig, feedback_transfer_function = pypt.subplots();
        youf, T = impulse(self.feedback);
        pypt.plot(T, youf.T);

        feedback_transfer_function.set_title("Feedback");
        feedback_transfer_function.set_ylabel('Voltage [V]');
        feedback_transfer_function.set_xlabel('Time [s]');

        pypt.show();
        pytm.sleep(0.5);

        # Poles and zeros:
        # print("Poles and zeros: \n");
        # damp(self.feedback);
        # pzmap(self.feedback);

        pytm.sleep(0.5);

        print("Root-Locus with feedback: \n");
        pyct.rlocus(self.feedback);

    # Adds a new system, which serves to make the control. In the case study it will be a step response:    
    def system_of_control(self):
        numerator = [];
        denominator = [];

        quantity_of_numerators = int(input("How many coefficients does the numerator have? "));
        quantity_of_denominators = int(input("How many coefficients does the denominator have? "));
        
        print("\nFor orders where the coefficients are zero, enter: 0.\n");
        
        for i in range(0, quantity_of_numerators):
            i = float(input("Enter, in the correct order, the coefficients of the numerator: "));
            numerator.append(i);

        numerator = pynp.array(numerator);
        print('');
        
        for j in range(0, quantity_of_denominators):
            j = float(input("Enter, in the correct order, the coefficients of the denominator: "));
            denominator.append(j);

        denominator = pynp.array(denominator);
        
        self.control_system = pyct.tf([[numerator]], [[denominator]]);
        print(self.control_system);

    # Analysis of this system along with the natural response:
    def in_series(self):
        self.series = pyct.series(self.control_system, self.system);
        print(self.series);
        print("Plot in series: \n");
        pytm.sleep(0.5);
        pypt.figure(3);

        fig, system_series = pypt.subplots();
        yout, T = impulse(self.series);
        pypt.plot(T.T, yout.T);

        system_series.set_xlabel('Time [s]');
        system_series.set_ylabel('Voltage [V]');
        system_series.set_title('Answer Step:');

        pypt.show(block = False);
        pytm.sleep(0.5);

        # Poles and zeros:
        # print("Poles and zeros: \n");
        # damp(self.series);
        # pzmap(self.series);

        pytm.sleep(0.5); 
        print("It is expected that in 'Open-loop' the gains do not change in root locus. \n");
        pyct.rlocus(self.series);
    

    # Analysis of this system in series with the natural response:
    def in_series_with_feedback(self): 
        self.feedback = pyct.feedback(self.series, sys2 = 1, sign = 1);
        print(self.feedback);
        print("Plot in series with feedback: \n");
        pytm.sleep(0.5);
        pypt.figure(1);

        fig, series_with_feedback = pypt.subplots();
        yout, T = impulse(self.feedback);
        pypt.plot(T.T, yout.T);

        series_with_feedback.set_xlabel('Time [s]');
        series_with_feedback.set_ylabel('Voltage [V]');
        series_with_feedback.set_title('Feedback Answer:');

        pypt.show(block = False);
        pytm.sleep(0.5);

        # Poles and zeros:
        # print("Poles and zeros: \n");
        # damp(self.feedback);
        # pzmap(self.feedback);

        pytm.sleep(0.5);

        print("It is expected that in 'Closed-loop' the gains change in root locus.");
        pyct.rlocus(self.feedback);
