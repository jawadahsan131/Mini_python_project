import json

class Simple_Reflex_Agent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp

    def perceive(self, current_temp):
        return current_temp

    def act(self,current_temp):
        if current_temp < self.desired_temp:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        return action
    
rooms = {
    "Living Room": 25,
    "Bedroom" : 20,
    "Kitchen" : 21,
    "Bathroom" : 25,
}

desired_temp = 23
agent = Simple_Reflex_Agent(desired_temp)

data = {}
for room, temperature in rooms.items():
    action = agent.act(temperature)
    data[room] = {"current_temperature": temperature, "action": action}

with open("Simple_reflex_results.json","w") as file:
    json.dump(data, file, indent = 4)

print("Results are stored successfully.")

class Model_Based_Reflex_agent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.heater_states = {}

    def perceive(self,current_temp):
        return current_temp
    
    def act(self, room, current_temp, stored_action):
        previous_state = self.heater_states.get(room, "off")
        stored_action_state = stored_action.split()[1]
        if current_temp < self.desired_temp:
            if previous_state == "off":
                self.heater_states[room] = "on"
                action = "Turn off "
            else:
                action = "Heater will remains on"
        else:
            if previous_state == "on":
                self.heater_states[room] = "off"
                action = "Turn off heater"
            else:
                action = "Heater will remains off"

        if stored_action == action:
            check = "Action matches sotred data."
        else:
            check = "Action differs from stored data."

        return action,check

with open("simple_reflex_results.json", "r") as file:
    stored_data = json.load(file)

rooms = {
    "Living Room": 18,
    "Bedroom": 20,
    "Kitchen": 21,
    "Bathroom": 26,    
}

desired_temp = 24
agent = Model_Based_Reflex_agent(desired_temp)

for room, temperature in rooms.items():
    stored_action = stored_data[room]["action"]
    action, check = agent.act(room, temperature, stored_action)
    print(f"{room}: Current temperature = {temperature}°C. {action}. {check}")
    