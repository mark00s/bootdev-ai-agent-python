def generate_content(client, messages, verbose, model="gemini-2.0-flash-001"):
    res = client.models.generate_content(
        model=model,
        contents=messages,
    )

    if verbose:
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")
        print("##############################################################")

    print(res.text)
