from fastapi import FastAPI
from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer
from typing import List
from pydantic import BaseModel

## Lets load from local Docker image or EFS disk instead of downloading it everytime(No S3 support), this reduces the container boot and initial request serving time.
model = M2M100ForConditionalGeneration.from_pretrained('models/m2m100_418M',config='models/m2m100_418M/config.json',local_files_only=True)
tokenizer = M2M100Tokenizer.from_pretrained('models/m2m100_418M',local_files_only=True)

## FastAPI initilization
app = FastAPI()

#Modelling payloads
class Records(BaseModel):
  id: str
  text: str

class Payload(BaseModel):
  records: List[Records]
  fromLang: str
  toLang: str

class Translate(BaseModel):
   payload: Payload

## Root route for a small help message!
@app.get("/")
async def root():
    return {"message": "Hello!, Please use /translation API for translation"}

## Actual Translation API
@app.post("/translation")
async def translator(translate: Translate):
    output_result = []
    text = translate.payload.records
    source_language = translate.payload.fromLang
    target_language = translate.payload.toLang
    for source_text in text:
        translated_result = translation(source_text.text,source_language,target_language)
        output_text = {"id": source_text.id, "text": translated_result}
        output_result.append(output_text)
        return {"result": output_result}

def translation(text, source_language, target_language):
    tokenizer.src_lang = source_language
    model_inputs = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.get_lang_id(target_language))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return result[0]