import boto3
import botocore.config
import json


from datetime import datetime

def code_generate_using_bedrock(code_topic: str) -> str:
    prompt = f"""<s>[INST]Human: Generate code for {code_topic}
    Assistant:[/INST]
    """

    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                               config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))
        response = bedrock.invoke_model(body=json.dumps(body), modelId="meta.llama3-70b-instruct-v1:0")

        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        print(response_data)
        code_details = response_data['generation']
        return code_details
    except Exception as e:
        print(f"Error generating the code: {e}")
        return ""

def save_code_details_s3(s3_key, s3_bucket, generated_code):
    s3 = boto3.client('s3')

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generated_code)
        print("Code saved to S3")
    except Exception as e:
        print("Error when saving the code to S3:", e)

def lambda_handler(event, context):
    event = json.loads(event['body'])
    code_topic = event['code_topic']

    generated_code = code_generate_using_bedrock(code_topic=code_topic)

    if generated_code:
        current_time = datetime.now().strftime('%H%M%S')
        s3_key = f"code-output/{current_time}.txt"
        s3_bucket = '<your_bucket_name>'
        save_code_details_s3(s3_key, s3_bucket, generated_code)
    else:
        print("No code was generated")

    return {
        'statusCode': 200,
        'body': json.dumps('Code Generation is completed')
    }

