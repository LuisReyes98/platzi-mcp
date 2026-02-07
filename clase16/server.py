from fastmcp import FastMCP

mcp = FastMCP('my-mcp-server')

root_context = {'message': 'Bienvenido', 'user_data': {}}


@mcp.tool()
def update_user_data(user_id: str, user_data: str) -> dict:

  root_context['user_data'][user_id] = user_data

  return root_context


@mcp.tool()
def get_user_data() -> dict:

  return root_context


if __name__ == '__main__':
  mcp.run()
