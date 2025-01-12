import json
import openai
from django.conf import settings
from coworking.models import CoworkingSpace

model = "gpt-4o-mini"
asistant_id = "asst_jZjkRA75jwQLNaKSnFcGg40t"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string"}},
            },
        },
    }
]


def wait_for_run_completion(client: openai.OpenAI, thread_id, run_id, sleep_interval=5):
    """

    Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            print(f"Run status: {run.status}")
            if run.completed_at:
                # Get messages here once Run is completed!
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                return response
            if run.status == "requires_action":
                tool_outputs = []

                for tool in run.required_action.submit_tool_outputs.tool_calls:
                    print(tool.function.name)
                    if tool.function.name == "get_weather":
                        print(tool.function.arguments)
                        tool_outputs.append(
                            {
                                "tool_call_id": tool.id,
                                "output": "31 grados celsius",
                            }
                        )
                    if tool.function.name == "get_coworking":
                        coworking = CoworkingSpace.objects.all()
                        coworking_string = ""
                        for cowork in coworking:
                            coworking_string += f"{cowork.name} en {cowork.location},  disponible: {cowork.is_available}, descripcion: {cowork.description}, precio por dia: {cowork.price_per_day}, precio por hora: {cowork.price_per_hour}, precio por mes: {cowork.price_per_month}, precio por semana: {cowork.price_per_week}\n"
                        tool_outputs.append(
                            {
                                "tool_call_id": tool.id,
                                "output": coworking_string,
                            }
                        )
                if tool_outputs:
                    run = client.beta.threads.runs.submit_tool_outputs_and_poll(
                        thread_id=thread_id,
                        run_id=run_id,
                        tool_outputs=tool_outputs,
                    )

        except Exception as e:
            print(f"Error: {e}")
            break


def get_gpt_response(prompt: str, thread_id: str):
    client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    message = client.beta.threads.messages.create(
        thread_id=thread_id, role="user", content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id,
        instructions="Respond to user message, but do not engage in political, religious, or controversial topics. Stick to the topic of the application, which is the rental of coworking spaces.",
    )

    response = wait_for_run_completion(
        client=client, thread_id=thread_id, run_id=run.id
    )

    return response


def create_thread_openai():
    client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    threadResponse = client.beta.threads.create()
    return threadResponse
