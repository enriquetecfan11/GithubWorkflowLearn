import requests
from bs4 import BeautifulSoup

# Function to scrape the Metro Madrid "La red en tiempo real" status
def scrape_metro_status():
    # URL of the Metro Madrid "La red en tiempo real"
    url = 'https://www.metromadrid.es/es'
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # If the response was successful, no Exception will be raised
    response.raise_for_status()
    
    # Initialize BeautifulSoup object to parse the content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize a dictionary to store the status of each line
    line_statuses = {}
    
    # Find all elements with class "list__lineas__element"
    line_elements = soup.find_all(class_='list__lineas__element')
    
    # Loop through each line element
    print("Estado de las líneas del metro de Madrid:")
    for line_element in line_elements:
        # Find the span with class "state--green" or "state--red" within the line element
        status_element = line_element.find('span', class_=["state--green", "state--red"])

        # Find the line number within the line element (if it exists)
        line_number = line_element.find('span', class_='list__lineas__element__numero')
        if line_number:
            line_number = line_number.text.strip()
        else:
            # For lines without a specific number, assign a number based on index
            line_number = str(line_elements.index(line_element) + 1)
        
        # Check if both status and line number are found
        if status_element and line_number:
            # Determine the status based on the class of the status element
            if 'state--green' in status_element['class']:
                status = 'Funcionamiento normal'
            elif 'state--red' in status_element['class']:
                status = 'Servicio interrumpido'
            else:
                status = 'No se ha podido determinar el estado'
            
            # If the line number corresponds to lines 13 to 16, update the name accordingly
            if line_number == '13':
                line_number = 'Ramal'
            elif line_number == '14':
                line_number = 'Metro ligero 1'
            elif line_number == '15':
                line_number = 'Metro ligero 2'
            elif line_number == '16':
                line_number = 'Metro ligero 3'
            
            # Add the status to the dictionary with the line number as key
            line_statuses[line_number] = status
    
    # Print the line statuses
    for line, status in line_statuses.items():
        print(f'{line}: {status}')
    
    # Return the dictionary containing the statuses
    return line_statuses

if __name__ == '__main__':
    scrape_metro_status()