- [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins)
- [ChatGPT plugins Doc](https://platform.openai.com/docs/plugins/introduction)
- [OpenAPI Specification](https://swagger.io/specification)


## Plugin development

```bash
[plugin-repo]
|- main.py
|- manifest.json
|- openapi.yaml
|- logo.png
`- ... # other
```

### manifest.json

[plugin-manifest](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest): Every plugin requires a ai-plugin.json file, which needs to be hosted on the API’s domain.

### openapi.yaml

[openapi-definition](https://platform.openai.com/docs/plugins/getting-started/openapi-definition): OpenAPI specification to document the API. The model in ChatGPT does not know anything about your API other than what is defined in the OpenAPI specification and manifest file. This means that if you have an extensive API, you need not expose all functionality to the model and can choose specific endpoints.

## Plugin Deploy (Replit)

- Open [Replit](https://replit.com) and click the `Create Repl` button.
- When the pop-up window appears, click the `Import from GitHub` button in the top right corner.
- In the GitHub URL field, enter `https://github.com/mirage-studio-io/chat-calculator-plugin` and select `Python` as the language.
- Then click the `Import from GitHub` button in the bottom right corner and wait for the initialization to complete.
- Click the `Run` button and wait for the execution to finish.

<!-- ## Local Development

```bash
# install dependencies
poetry install

# run the service
poetry run python main.py
``` -->

## CALCULATOR API

### Addition
```bash
curl -X GET http://0.0.0.0:5002/calculator/add/5.0/3.0 \
 -H 'Content-Type: application/json'
```

### Subtraction
```bash
curl -X GET http://0.0.0.0:5002/calculator/subtract/5.0/3.0 \
 -H 'Content-Type: application/json'
 ```
 
### Multiplication
```bash
curl -X GET http://0.0.0.0:5002/calculator/multiply/5.0/3.0 \
 -H 'Content-Type: application/json'
 ```
 
### Division
```bash
curl -X GET http://0.0.0.0:5002/calculator/divide/6.0/3.0 \
 -H 'Content-Type: application/json'
 ```
 
### Power
```bash
curl -X GET http://0.0.0.0:5002/calculator/power/2.0/3.0 \
 -H 'Content-Type: application/json'
 ```
 
### Square Root
```bash
curl -X GET http://0.0.0.0:5002/calculator/sqrt/9.0 \
 -H 'Content-Type: application/json'
 ```
 
 MIT License - Mirage Studio
