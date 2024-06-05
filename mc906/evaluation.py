from time import sleep
from groq import Groq, RateLimitError
import pandas as pd
from tqdm import tqdm
from openai import OpenAI
groq_client = Groq(
    api_key=""
)

openai_client = OpenAI(
     api_key="sk-"
)

def llm_call(
        message,
        model,
        temperature=0.2,
        top_p=0.95,
    ):
        messages = [
            {
                "role": "user",
                "content": message,
            }
        ]
        response = openai_client.chat.completions.create(
              messages=messages,
              model=model,
              top_p=top_p,
              temperature=temperature,
          )
        return str(response.choices[0].message.content)

def load_gender_dataset():
    return pd.read_csv("gender.csv")

def load_racism_dataset():
    return pd.read_csv("racism.csv")

def evaluate(dataset: pd.DataFrame, model: str, dataset_name: str):
    llm_responses = []
    prompts = dataset["prompt"].astype(str).tolist()

    for prompt in tqdm(prompts, desc=f"Evaluating {dataset_name} with {model}", total=len(prompts)):
        try:
            response = llm_call(prompt, model)
            llm_responses.append(response)
        except RateLimitError:
            sleep(40)
            continue

    dataset["llm_response"] = llm_responses

    final_path = f"evaluations/{model}/{model}_{dataset_name}.csv"
    dataset.to_csv(final_path, index=False)

    return dataset

if __name__ == "__main__":
    racism_dataset = load_racism_dataset()
    gender_dataset = load_gender_dataset()

    # evaluate(racism_dataset, "gpt-4o", "racism")
    # evaluate(gender_dataset, "gpt-4o", "gender")


