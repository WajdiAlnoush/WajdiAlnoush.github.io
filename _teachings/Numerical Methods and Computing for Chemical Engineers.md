---
layout: course
title: Numerical Methods and Computing for Chemical Engineers 
university: McMaster University
description: This course (CHEMENG 2E04) focuses on the formulation and solution of various engineering problems. A variety of techniques for numerical solution of linear and nonlinear model equations are reviewed, including algebraic and ordinary differential equations, and the use of curve-fitting and interpolation methods.
instructor: Dr. Jake Nease | Dr. Stuart Linely
year: 2020-2024
term: Fall
# location: Main Campus, Room 301
# time: Tuesdays and Thursdays, 10:00-11:30 AM
course_id: intro-machine-learning
schedule:
  - module: 1
    date: Sept 5
    topic: Linear Systems of Equations
    description: 
        <ul>
          <li>Overview of course structure</li>
          <li>Linear system modeling</li>
          <li>Expansion to discretized systems</li>
        </ul>
    materials:
      - name: Syllabus
        url: /assets/pdf/example_pdf.pdf
      - name: Slides
        url: /assets/pdf/example_pdf.pdf

  - module: 2
    date: Sept 12
    topic: Linear System Solutions - Elimination Methods
    description: 
        <ul>
          <li>Gauss elimination</li>
          <li>Gauss-Jordan elimination</li>
          <li>LU decomposition</li>
          <li>Trade-Offs and applications</li>
          <li>Pivoting</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Assignment 1
        url: /assets/pdf/example_pdf.pdf

  - module: 3
    date: Sept 19
    topic: Linear System Solutions - Iterative Methods
    description: 
        <ul>
          <li>Jacobi method</li>
          <li>Gauss-Seidel method</li>
          <li>Diagonal dominance</li>
          <li>Smoothing</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Coding Lab
        url: https://github.com/

  - module: 4
    date: Sept 26
    topic: Nonlinear Systems - Formulation and Bracketing
    description: 
        <ul>
          <li>Formulating nonlinear problems</li>
          <li>Bisection for univariate solutions</li>
          <li>Regula-Falsi for univariate equations</li>
          <li>Rates of convergence</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Assignment 2
        url: /assets/pdf/example_pdf.pdf

  - module: 5
    date: Oct 3
    topic: Nonlinear Systems - Open Methods and Multivariate Solutions
    description: 
        <ul>
          <li>Secant method</li>
          <li>Review of Taylor Series expansion</li>
          <li>Newton-Raphson method</li>
          <li>Multivariate Newton-Raphson method</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Review Materials
        url: /assets/pdf/example_pdf.pdf

  - module: 6
    date: Oct 10
    topic: Curve Fitting - Regression
    description: 
        <ul>
          <li>Concept of regression and optimization</li>
          <li>Linear regression</li>
          <li>Polynomial regression</li>
          <li>Basis function regression</li>
        </ul>
  - module: 7
    date: Oct 17
    topic: Curve Fitting - Interpolation
    description: 
        <ul>
          <li>Lagrange polynomials</li>
          <li>Splines</li>
          <li>Data scaling and normalization</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Assignment 3
        url: /assets/pdf/example_pdf.pdf

  - module: 8
    date: Oct 24
    topic: Numerical Differentiation
    description: 
        <ul>
          <li>Finite differences</li>
          <li>Partial derivatives</li>
          <li>Derivatives via curve fitting</li>
          <li>Error analysis</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Coding Lab
        url: https://github.com/

  - module: 9
    date: Oct 24
    topic: Numerical Integration
    description: 
        <ul>
          <li>Newton-Cotes formulas and error analysis</li>
          <li>Richardson extrapolation</li>
          <li>Romberg integration</li>
          <li>Multiple integrals</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Coding Lab
        url: https://github.com/

  - module: 10
    date: Oct 24
    topic: Univariate and Multivariate Differential Equations
    description: 
        <ul>
          <li>Defining ODEs</li>
          <li>Methods of solving ODEs</li>
          <li>Multivariate Euler’s, and RK4 methods</li>
        </ul>
    materials:
      - name: Lecture Notes
        url: /assets/pdf/example_pdf.pdf
      - name: Coding Lab
        url: https://github.com/
---
<style>table th:nth-child(2),table td:nth-child(2) {display: none;}</style>  
<style>table th:nth-child(4),table td:nth-child(4) {display: none;}</style> 

## Learning Objectives

By the end of this course, students will be able to:

 - Recognize when numerical methods should be applied as a part of a solution to a variety of chemical engineering (and other) problems or opportunities.
 - Formulate mathematical models of common engineering unit operations and processes.
- Identify the appropriate algorithm or numerical method suitable for the solution.
- Break down how an algorithm works based on fundamental mathematical concepts.
- Implement algorithms using calculators and (more importantly) software tools.
- Derive algorithms for new problems based on a fundamental understanding of the objective.
- Use a numerical solution to help solve the original problem of interest.
- Identify the critical differences, advantages, and disadvantages of numerical versus analytical techniques.

<!-- ## Prerequisites

- Basic knowledge of linear algebra and calculus
- Programming experience in Python
- Probability and statistics fundamentals -->

## Textbooks

- A. Gilat, V. Subramaniam: Numerical Methods for Engineers and Scientists. Wiley.


<!-- ## Grading

- Assignments: 40%
- Midterm Exam: 20%
- Final Project: 30%
- Participation: 10% -->
