# CodeSmith

CodeSmith is a serverless application built within the AWS ecosystem. It utilizes AWS Lambda for executing the code generation logic, Amazon Bedrock for accessing the `meta.llama3-70b-instruct-v1:0` model to generate code based on user requests, and Amazon S3 for storing the generated code.

## Architecture Overview

![code gen project](https://github.com/avd1729/CodeSmith/assets/94891044/693ebef9-97bd-4fb0-b9b1-8f5eebc85ec0)


The project architecture can be summarized as follows:

- **AWS Lambda**: AWS Lambda functions are used to execute the code generation logic. Each Lambda function is triggered by HTTP requests from Amazon API Gateway.

- **Amazon Bedrock**: The project leverages Amazon Bedrock to access the `meta.llama3-70b-instruct-v1:0` model. This model is responsible for generating code based on the user's request.

- **Amazon API Gateway**: Amazon API Gateway acts as the entry point for user requests. Users send POST requests to the API Gateway, which triggers the associated Lambda function.

- **Amazon S3**: The generated code is stored in Amazon S3 buckets. After code generation, the Lambda function uploads the generated code to an S3 bucket for future retrieval.

## Usage

To use the CodeSmith:

1. Send a POST request to the provided API Gateway endpoint with the required parameters (e.g., code topic).
2. The API Gateway triggers the corresponding Lambda function, which accesses the Bedrock model to generate code.
3. The generated code is then stored in the designated S3 bucket.

## Setup

To set up the CodeSmith:

1. Ensure you have an AWS account with appropriate permissions to create Lambda functions, API Gateway endpoints, access Bedrock models, and interact with S3 buckets.
2. Deploy the Lambda function code to your AWS account.
3. Set up an API Gateway endpoint to trigger the Lambda function.
4. Configure access to the `meta.llama3-70b-instruct-v1:0` model in Amazon Bedrock.
5. Set up an S3 bucket to store the generated code.

## Contributing

Contributions to the CodeSmith are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).
