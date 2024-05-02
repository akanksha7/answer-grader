# Answer Evaluator: Revolutionizing the Grading Process

## Introduction

Imagine a world where grading stacks of essays and exams doesn't take hours. A world where educators can spend more time providing constructive feedback and less time on tedious marking. Recognizing this need, our team embarked on a journey to develop an innovative solution – the **Answer Evaluator**. Inspired by the challenges faced by educators in grading student assessments, our application aims to streamline the evaluation process, saving valuable time and providing insightful feedback to both students and teachers.

## Project Inspiration

The inspiration behind the Answer Evaluator stems from firsthand experiences of educators grappling with the arduous task of grading a multitude of student responses. Whether it's essays, assignments, or exams, assessing each submission against a predefined rubric demands meticulous attention to detail and consumes precious hours of a teacher's time. Moreover, as students ourselves, we understand the frustration of waiting for grades and the uncertainty surrounding evaluation criteria. By leveraging the power of artificial intelligence, we envisioned a tool that could alleviate these concerns and provide a standardized approach to grading.

## How it Works

The Answer Evaluator is a user-friendly web application designed to simplify the grading process for educators. Leveraging the power of Google Gemini's advanced AI models, our app offers a seamless experience for evaluating both text-based and handwritten answers. Here's how it works:

1. **Upload Answer**: The evaluator can upload the student's answer text or even a picture of a handwritten response. This flexibility ensures that assessments in various formats can be easily processed.

2. **Upload Rubric**: Alongside the answer, the evaluator uploads the corresponding rubric or marking scheme, specifying the maximum marks allotted for that particular question.

3. **Single-Click Evaluation**: With just a click of a button, the app initiates the evaluation process, providing a score for the student's answer within a few seconds. This streamlined approach allows evaluators to assess multiple submissions rapidly.

4. **Customizable Marking Type**: The Answer Evaluator empowers evaluators to choose from different marking types – lenient, normal, or strict. Depending on the selected option, the app adjusts its grading criteria, providing flexibility to accommodate varying assessment standards.

5. **Insightful Feedback**: In addition to assigning a score, the app generates detailed feedback, outlining the reasons behind the evaluation. This feature fosters transparency and facilitates constructive communication between educators and students.

## Technological Details

### Backend
- **Google Gemini**: The backbone of our application, Google Gemini's cutting-edge AI models power the evaluation process. The Gemini-Pro model analyzes text-based answers, while Gemini-Pro-Vision handles image-based submissions, ensuring comprehensive assessment capabilities.

### Frontend
- **Streamlit**: The frontend interface is developed using Streamlit, a user-friendly framework for building data-driven web applications in Python. Its intuitive design enables seamless interaction and navigation for both educators and students.

## Addressing Challenges
### Consistency in Evaluation
During testing, we encountered a significant challenge related to the consistency of evaluations. Despite using the same input and rubric, the generated scores exhibited slight variations, which could potentially undermine the reliability of the application. To mitigate this issue, we fine-tuned the parameters of the Gemini-Pro model, reducing the temperature parameter to minimize randomness and ensure consistent outputs.


## Benefits and Impact

The Answer Evaluator holds immense potential to revolutionize the grading process in education. By automating tedious tasks and providing valuable insights, it offers the following benefits:

- **Time Efficiency**: Eliminates the manual effort involved in grading, allowing educators to focus on more meaningful aspects of teaching and learning.
- **Consistency**: Ensures uniformity and fairness in evaluation, regardless of the volume of submissions or the evaluator's subjective biases.
- **Enhanced Feedback**: Provides students with detailed feedback, enabling them to understand their strengths and areas for improvement.
- **Scalability**: Adaptable to various educational contexts, from traditional classrooms to online learning platforms, catering to the evolving needs of educators worldwide.

In essence, the Answer Evaluator is not just a tool; it's a catalyst for educational transformation, empowering educators and students alike to thrive in an increasingly digital world.

<img width="1455" alt="Screenshot 2024-05-02 at 3 46 31 PM" src="https://github.com/akanksha7/answer-grader/assets/18654204/83d70674-a053-4647-a7fd-b7721cccdbfb">

