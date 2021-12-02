
# Zendesk-Ticket-Viewer

This is a tool to view your Zendesk tickets. The application is written in **python**

Contents

1. [What can it do](#what-can-it-do)
2. [How does it work](#how-does-it-work)
3. [Instructions](#instructions)
4. [Tests](#tests)

## What can it do

1. Show all tickets
2. Display details of a ticket

## How does it work

### Authentication
The application uses OAuth2 access token for authentication. The token's scope is read-only. 
### Get all tickets
To show all tickets, it makes a call to Zendesk API for 25 tickets; the response from the api is stored into a data structure in a singleton class. Users can page through tickets if there are more than 25 tickets. The application uses cursor pagination.
### Get a single ticket details
 When a user wants to view a single ticket, it first checks whether this ticket was received in the last api call to fetch 25 tickets. If it is in the cache(Singleton's data structure); and it has been less than 45 seconds since cache update, it returns the ticket from cache. Tickets get updated frequently, so 45 seconds is a reasonable time frame. Else, it makes the api call to fetch the ticket information.
## Instructions

### Environment requirements

1. Python3
2. Terminal (Unix shells)

### Running the application

#### Step 1:

Clone the project. It is recommended that you set up a virtual environment after cloning the repo.

#### Step 2:

Run `make init` in the terminal to install therequired packages.

#### Step 3 (Optional):

Update the credentials and subdomain URL in `config/config.py` file.

#### Step 4:

Run `make run` in the terminal to start the application.


## Tests

Files that contain tests have "test_" prefix. The project include tests for api calls and output parser.

Run `make test` in a terminal to run all tests.



