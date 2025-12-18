import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import schema_get_files_info
from call_functions import available_functions
from call_function import call_function
import sys


def generate_content(client, messages, verbose):
    # ... code for handling generate_content and function calls ...
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    if response.usage_metadata is None:
        raise RuntimeError("Meta data is none!")

    if verbose:
        #print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    for item in response.candidates:
        messages.append(item.content)

    tool_list = []

    if not response.function_calls:
        #print("Response:")
        #print(response.text)
        #return
        pass
            
    else:
        for item in response.function_calls:
            function_call_result = call_function(item)

            if (
                not function_call_result.parts
                or not function_call_result.parts[0].function_response
                or function_call_result.parts[0].function_response.response is None
            ):
                raise Exception("Function call returned no response")
            
            tool_list.append(function_call_result.parts[0])

            
            #if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

            print(f"Calling function: {item.name}({item.args})")

    new_messages = types.Content(role="user", parts=tool_list)
    messages.append(new_messages)

    if not response.function_calls:
        return response.text
    else:
        return None


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if api_key is None:
        raise RuntimeError("API Key not found!")
    
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    counter = 1
    while counter <= 20:
        try:
            counter += 1
            response = generate_content(client, messages, args.verbose)
            if response:
                print("Final response:")
                print(response)
                break

            

        except Exception as e:
            print(f"Error {e}")
            sys.exit()



    #print("Debug schema:", available_functions)
    #print("DEBUG function_calls raw:", response.function_calls)




        #print(response.text)

    #print(response.text)


if __name__ == "__main__":
    main()
