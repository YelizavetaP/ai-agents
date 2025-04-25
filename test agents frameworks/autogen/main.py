import autogen

def main():
    config_list = autogen.config_list_from_json(
        # config model and api key
        env_or_file="OAI_CONFIG_LIST.json"
    )

    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": config_list
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="UserProxy",
        # if human is a part of the loop
        human_input_mode="NEVER",
        code_execution_config={
            "work_dir": "code",
            "use_docker": False
        }
    )

    user_proxy.initiate_chat(
        assistant,
        # task
        message="Plot a chart of META and Tesla stock price from 2020 to 2024"
    )

if __name__ == "__main__":
    main()


