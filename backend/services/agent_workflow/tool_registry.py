from langchain_core.tools import Tool, StructuredTool
from backend.services.agent_workflow.tool_functions.check_current_time_tool import get_current_time
from backend.services.agent_workflow.tool_functions.wikipedia_search_tool import search_wikipedia
from backend.services.agent_workflow.tool_functions.web_search_tool import serpapi_search
from backend.services.agent_workflow.tool_functions.check_stock_price_tool import get_stock_price
from backend.services.agent_workflow.tool_functions.check_weather_tool import get_weather
from backend.services.agent_workflow.tool_functions.convert_currency_tool import convert_currency
from backend.services.agent_workflow.tool_functions.search_youtube import search_youtube_videos
from backend.services.agent_workflow.tool_functions.e_commerce_product_search_tool import e_commerce_search
from backend.services.agent_workflow.tool_functions.indian_holiday_lookup_tool import lookup_indian_holidays
from backend.services.agent_workflow.tool_functions.check_train_status_tool import get_train_live_status, TrainStatusInput
from backend.services.agent_workflow.tool_functions.train_pnr_status_checker_tool import get_pnr_status
from backend.services.agent_workflow.tool_functions.flight_status_checker_tool import get_flight_status
from backend.services.agent_workflow.tool_functions.fd_rate_checker_tool import get_fd_rates
from backend.services.agent_workflow.tool_functions.search_recharge_plans_tool import search_recharge_plans


tools = [
    Tool(
        name="Time",
        func=get_current_time,
        description="Useful for when you need to know the current time.",
    ),
    Tool(
        name="Wikipedia",
        func=search_wikipedia,
        description="Use this tool to look up general knowledge or facts about people, places or topics using Wikipedia.",
    ),
    Tool(
        name="Google Search",
        func=serpapi_search,
        description="Use this tool for general web searches, news, events, or when no specific product listing is needed or anything that Wikipedia cannot answer.",
    ),
    Tool(
        name="Stock Price Checker",
        func=get_stock_price,
        description="Use this tool to get real-time stock prices. Input should be a company ticker symbol like 'TSLA' or 'AAPL'.",
    ),
    Tool(
        name="Weather",
        func=get_weather,
        description="Use this tool to check the current weather of a city. Input should be a city name like 'Mumbai' or 'New York' or using the IP of the user to detect location automatically.",
    ),
    Tool(
        name="Currency Converter",
        func=convert_currency,
        description="Use this to convert between currencies, like '100 USD to INR'."
    ),
    Tool(
        name="YouTube Video Search",
        func=search_youtube_videos,
        description="Use this to find recent YouTube videos about a topic or person."
    ),
    Tool(
        name="E-commerce Product Search",
        func=e_commerce_search,
        description="Use this tool to find and recommend actual products and listings (like phones, earbuds, laptops, etc.) from Amazon and Flipkart. "
        "Always prefer this tool for any product-related questions."
        "Include the tool output directly in your final answer instead of paraphrasing."
    ),
    Tool(
        name="Indian Holiday Lookup",
        func=lookup_indian_holidays,
        description="Use this to check if a specific date is a public holiday in India, or to see upcoming Indian holidays.",
    ),
    StructuredTool.from_function(
        name="Train Live Status Checker",
        description="Use this tool to get the live running status of a train. Input should include 'train_number' and optional 'start_day' (default is 1).",
        func=get_train_live_status,
        args_schema=TrainStatusInput,
    ),
    Tool(
        name="PNR Status Checker",
        func=get_pnr_status,
        description="Check Indian Railways PNR status using a 10-digit PNR number like '1234567890'."
    ),
    Tool(
        name="Flight Status Checker",
        func=get_flight_status,
        description="Get current status of a flight using its IATA flight code, e.g. 'AI101' or 'UA246'."
    ),
    Tool(
        name="FD Rates Checker",
        func=get_fd_rates,
        description=(
            "Fetch latest fixed deposit interest rates from BankBazaar. Always show rates from other banks as well if available"
        )
    ),
    Tool(
    name="Recharge Plan Search",
    func=search_recharge_plans,
    description="Fetch real-time prepaid recharge plans for telecom operators like Airtel, Jio, VI via trusted sources."
),
]