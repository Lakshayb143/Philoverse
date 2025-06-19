

# if __name__ == "__main__":
#     import asyncio

#     philosopher_factory = PhilosopherFactory()
#     philosopher = philosopher_factory.get_philosopher("plato")

#     async def main():
#         response, _ = await get_response(
#             messages=["Hello, I'm Paul. What is the meaning of life?"],
#             philosopher_id=philosopher.id,
#             philosopher_name=philosopher.name,
#             philosopher_perspective=philosopher.perspective,
#             philosopher_style=philosopher.style,
#             philosopher_context="",
#         )
#         print(response)

#     asyncio.run(main())