# Instructions  

## Task 1: Set Up Your App

### Step 1

This program uses the following widgets:

- App
- ButtonGroup
- Text
- PushButton

Make sure that all of the widgets have been imported on the top line of code. 

### Step 2

Now make sure that you have included the line of code that creates the app and the final line of code that displays the app. 

**Tip:** Look at your last project if you are unsure of what to do.

## Task 2: Build The App

### Step 1

In the workbook, take a look at the layout for the app that you are going to build. Note the required widgets and the order in which they appear.

### Step 2
Make sure that each widget has its own unique identifier.

Here is a table to help you with the identifiers of each widget. 

| Identifier   | Widget      |
| ------------ | ----------- |
| instruction  | Text        |
| joke_choice  | ButtonGroup |
| joke_button  | PushButton  |
| display_joke | Text        |

### Step 3

The new widget that you need to use is the ButtonGroup widget. Here is a code snippet:

```python3
ButtonGroup
identifier = ButtonGroup(app, options=["op1", "op2"], selected="op1")
```

This code snippet can be used to create a list of options. The identifier should be replaced with your unique identifier. “op1”, ”op2” are the list items. You can add more as long as you add a comma and surround the option with speech marks. The selected part is where you choose which option should initially be selected in the list.  

## Task 3: Create the Jokes Function

### Step 1

Make sure that your PushButton calls the jokes function when it is pressed. 

**Tip:** Look at your previous app to remember how to properly set up the PushButton.  

### Step 2

The jokes function needs to be defined at the beginning of the code. You should place this underneath the import statement.

To access the selected option from the ButtonGroup, you need to use:

```python3
identifier.value
```

Below is a code snippet to get you started with the jokes function. 

```python3
def jokes():
    if joke_choice.value == "Stick":
        display_joke.value = "What is brown and sticky? A stick!"
```

Complete the jokes function so that it covers all the jokes that a user can select from the ButtonGroup. 

- Joke 2: What is pink and fluffy? Pink fluff!
- Joke 3: Why did the chicken cross the road? To buy some toilet paper!
- Joke 4: What happens to a frog's car when it breaks down? It gets toad away!

### Step 3

Now test your program. At this point it should be fully functional.

## Explorer Tasks

- Separate the jokes and the punchlines. The user should be able to click one button that reveals the start of the joke, and press a second button that reveals the punchline. 
- Visit the guizero documentation page and look at the ‘Recipes’ that have been made available for you to use. These are code snippets that you can incorporate into your own programs. 
