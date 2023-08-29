# OCR and Text Analysis API

## Project Introduction

This project offers an API developed in the field of Optical Character Recognition (OCR) and text analysis. The API provides the capability to recognize text in images submitted by users and identifies sensitive data within this text, returning the results. Additionally, it caches previously processed images to provide fast responses when requested again.

## Sensitive Data Types

This API recognizes and validates the following sensitive data types:

- Phone Number 
- ID Number 
- Credit Card Number 
- Plate 
- Date 
- Email 
- Domain
- URL 
- Hash 
- Combolist
## API Usage

To use the API, follow the steps below::

1. Go to the Address:

   To explore the usage and endpoints of the API, go to this link: http://localhost:8081/docs. This link will redirect you to the Swagger documentation.

2. Upload an Image for Visual Analysis:

   In the Swagger UI interface, select the /analyze_image/ endpoint, which performs visual analysis with the API. Click the "Try it out" button to view the required parameters for uploading an image.

3. Upload an Image File:

   Add an image file to the "image" parameter. This will be used for the visual analysis process.

4. Send the Request and View the Results:

   After adding the image file, click the "Execute" button to send the request. The API will analyze the image and display the results to you.

## Sample Responses

![ocr1](https://github.com/Huseyinn1/OCR-Analysis-API/assets/88551122/8894c2ea-472f-4cf2-b376-8d2032753b4a)

![ocr-2](https://github.com/Huseyinn1/OCR-Analysis-API/assets/88551122/e4d37662-12ce-47f3-81b0-5ca4859fab0d)
## Contribution
  -We welcome all kinds of contributions and suggestions. Please fork this repository and make your contributions. Then create a Pull Request to share the changes.
