import json
import boto3

client = boto3.client('bedrock-agent')
def datasource_knowledgebase_sync(kb_dataSourceId,kb_knowledgeBaseId):
    response = client.start_ingestion_job(
    dataSourceId=kb_dataSourceId,
    knowledgeBaseId=kb_knowledgeBaseId
    )
    return response


def lambda_handler(event, context):
    
    response=datasource_knowledgebase_sync("3NCMNFMJRM","NBJ8IH5DIK")
    print("hello")
    return {
        'statusCode': 200,
        'body': "synced the database"
    }
