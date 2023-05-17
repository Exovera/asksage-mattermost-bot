# AskSage Mattermost Integration

The [AskSage](https://www.asksage.ai) Mattermost Bot is a powerful integration tool for your Mattermost instance. It functions as a virtual agent, facilitating seamless interactions with [AskSage](https://www.asksage.ai), an advanced AI knowledge base, directly through your Mattermost channels. This bot is designed to enhance team productivity and efficiency by answering queries, providing intelligent insights, and assisting with various tasks in real-time.

## Table of Contents

- [Mattermost](#mattermost)
- [AskSage](#asksage)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Mattermost

Mattermost is a flexible, open-source messaging platform that enables secure team collaboration. It's a perfect environment for integrating your AskSage bot.

A preview version of Mattermost is included in the Docker Compose file for this project. This allows you to spin up a development version of Mattermost locally, which can be used for testing and developing the AskSage bot.

### Getting Started with Mattermost

To run the preview version of Mattermost, use the following command:

```bash
docker-compose up mattermost
```
This will start a local Mattermost instance. The first time you access the instance, you'll need to set up the admin account. Follow the prompts to create a username, password, and email address for the admin account.

## Enabling Bot Accounts
To use the AskSage bot, you'll need to enable bot accounts in Mattermost. To do this:

1. Log in to Mattermost as the admin user.
2. Click on the menu button (three horizontal lines) in the top left corner.
3. Navigate to "System Console" > "Integrations" > "Bot Accounts".
4. Set "Enable Bot Account Creation" to "true".
5. Click "Save".

### Creating the AskSage Bot Account

Next, you'll need to create the AskSage bot account:

1. Navigate to "Main Menu" > "Integrations".
2. Click "Bot Accounts".
3. Click "Add Bot Account".
4. Enter "AskSage" as the bot's username.
5. Configure the access control as required for your project.
6. Click "Create Bot Account".

Once the bot account is created, you'll be provided with an access token. This token will be used to authenticate the AskSage bot in Mattermost.

Keep this token secure and do not share it with unauthorized individuals. You'll need to enter this token as the `MATTERMOST_BOT_TOKEN` environment variable when setting up the bot.

With these steps completed, your local Mattermost instance is ready for use with the AskSage bot.

## AskSage
To use the AskSage Mattermost Bot, you'll need an AskSage account. If you don't have one, please sign up for an account on the [AskSage website](https://www.asksage.ai). You will need a paid AskSage account to be able to use this service. You can [sign up](https://chat.asksage.ai/register) for an account here. Please note that AskSage is not available in all countries. 

Once you have an account, you'll receive a username and password. These will serve as the credentials for the bot, allowing it to interact with the AskSage AI and provide responses to your queries. Please remember to keep these credentials secure and do not share them with unauthorized individuals.

## Installation

This section will guide you through the installation of the AskSage Mattermost Bot. The bot is packaged as a Docker container, which simplifies the installation process and ensures that the bot runs in a self-contained environment.

### Prerequisites

- Docker
- Docker-compose
- A [Mattermost](https://mattermost.com) instance you have admin access to

### Steps

1. Clone the AskSage Mattermost Bot repository:

    ```bash
    git clone https://github.com/yourusername/asksage-mattermost-bot.git
    cd asksage-mattermost-bot
    ```

2. Create a new file named `.env` in the root of the project, and fill it with your environment variables:

    ```bash
    touch .env
    ```

    Edit the `.env` file with the following variables:

    ```bash
    SAGE_EMAIL_ACCOUNT=your_sage_email_account
    SAGE_API_PASSWORD=your_sage_api_password
   
    MATTERMOST_BOT_TOKEN=your_mattermost_bot_token
    MATTERMOST_URL=your_mattermost_url
    MATTERMOST_TEAM=your_mattermost_team
    ```

    Ensure you replace the placeholders (`your_sage_api_password`, `your_mattermost_bot_token`, etc.) with your actual data.


3. Build and run the Docker container using Docker Compose:

    ```bash
    docker-compose build
    docker-compose up
    ```

    The AskSage Mattermost Bot is now up and running in a Docker container and should be connected to your Mattermost instance. You can start interacting with it in the designated Mattermost channels.

Please note that the bot needs appropriate permissions on your Mattermost instance to function correctly. This might include posting and reading messages, reacting to posts, and more, depending on your use case.


## Usage

Using the AskSage Mattermost Bot is straightforward. After successful installation and configuration, the bot will be ready to accept commands and provide responses.

To interact with the bot, simply type the following command in your Mattermost chat. You can either directly message the bot privately, or add it to a public channel:

```bash
=sage ask <your message>
```

## License

This project is licensed under the terms of the Apache 2.0 open source license. This allows you to freely use, modify, and distribute this software, under specific conditions outlined in the license.

For the specific terms and conditions of the Apache 2.0 license, please refer to the `LICENSE` file in the root directory of this project, or visit the [Apache 2.0 License page](http://www.apache.org/licenses/LICENSE-2.0).

