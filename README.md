**Build Agentville**

## Flask Application Design

### HTML Files

- **agentville.html**

   - Contains the main interface of the application.
   - Provides options for users to create, view, edit, and delete agents.
   - Includes a table to display the list of all agents.
   - Includes forms for creating, editing, and deleting agents.

### Routes

- **@app.route('/agentville', methods=['GET', 'POST'])**

   - Handles the display of the main interface.
   - If the request is a GET request, it renders the 'agentville.html' template.
   - If the request is a POST request, it processes the form data and performs the appropriate CRUD operations on the database.

- **@app.route('/create_agent', methods=['POST'])**

   - Handles the creation of new agents.
   - Validates the form data for completeness and correctness.
   - Inserts the new agent into the database.
   - Redirects to the main interface ('/agentville') upon successful creation.

- **@app.route('/edit_agent/<int:id>', methods=['GET', 'POST'])**

   - Handles the editing of existing agents.
   - If the request is a GET request, it retrieves the agent with the specified ID from the database and renders the 'agentville.html' template with the agent's data pre-populated in the form.
   - If the request is a POST request, it validates the form data, updates the agent's data in the database, and redirects to the main interface ('/agentville') upon successful update.

- **@app.route('/delete_agent/<int:id>', methods=['POST'])**

   - Handles the deletion of existing agents.
   - Deletes the agent with the specified ID from the database.
   - Redirects to the main interface ('/agentville') upon successful deletion.