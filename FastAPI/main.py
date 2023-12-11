from automata.fa.dfa import DFA
from automata.pda.dpda import DPDA
from automata.fa.nfa import NFA
from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/dpda")
async def automata(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    stack_symbols = set(info.get("stack_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    initial_stack_symbol = info.get("initial_stack_symbol","")
    final_states = set(info.get("final_states", []))
    acceptance_mode = info.get("acceptance_mode", "")

    input_w = info.get("input_w", "")

    if len(states) == 0:
        return {"message": "States cannot be empty"}
    if len(input_symbols) == 0:
        return {"message": "Input symbols cannot be empty"}
    if len(stack_symbols) == 0:
        return{"message": "Stack symbols cannot be empty"}
    if len(transitions) == 0:
        return {"message": "Transitions cannot be empty"}
    if initial_state == "":
        return {"message": "Initial state cannot be empty"}
    if initial_stack_symbol == "":
        return {"message": "Initial stack symbol cannot be empty"}
    if len(final_states) == 0:
        return {"message": "Final states cannot be empty"}
    if acceptance_mode == "":
        return {"message": "Acceptance mode cannot be empty"}
    if input_w == "":
        return {"message": "Input string cannot be empty"}    
    
    dpda = DPDA(
        states=states,
        input_symbols=input_symbols,
        stack_symbols=stack_symbols,
        transitions=transitions,
        initial_state=initial_state,
        initial_stack_symbol=initial_stack_symbol,
        final_states=final_states,
        acceptance_mode=acceptance_mode
    )

    if dpda.accepts_input(input_w):
        return {"message": "Accepted"}
    else:
        return {"message": "Rejected"}


@app.post("/nfa")
async def automata(request: Request):
    info = await request.json()
    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    transitions = dict(info.get("transitions", {}))
    initial_state = info.get("initial_state", "")
    final_states = set(info.get("final_states", []))

    input_w = info.get("input_w", "")
    
    if len(states) == 0:
        return {"message": "States cannot be empty"}
    if len(input_symbols) == 0:
        return {"message": "Input symbols cannot be empty"}
    if len(transitions) == 0:
        return {"message": "Transitions cannot be empty"}
    if initial_state == "":
        return {"message": "Initial state cannot be empty"}
    if len(final_states) == 0:
        return {"message": "Final states cannot be empty"}
    if input_w == "":
        return {"message": "Input string cannot be empty"}

    nfa = NFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    if nfa.accepts_input(input_w):
        return {"message": "Accepted"}
    else:
        return {"message": "Rejected"}



@app.post("/dfa")
async def automata(request: Request):
    info = await request.json()

    states = set(info.get("states", []))
    input_symbols = set(info.get("input_symbols", []))
    initial_state = info.get("initial_state", "")
    final_states = set(info.get("final_states", []))
    transitions = dict(info.get("transitions", {}))

    input_w = info.get("input_w", "")

    # Check if the DFA is valid

    if len(states) == 0:
        return {"message": "States cannot be empty"}
    if len(input_symbols) == 0:
        return {"message": "Input symbols cannot be empty"}
    if initial_state == "":
        return {"message": "Initial state cannot be empty"}
    if len(final_states) == 0:
        return {"message": "Final states cannot be empty"}
    if len(transitions) == 0:
        return {"message": "Transitions cannot be empty"}
    if input_w == "":
        return {"message": "Input string cannot be empty"}

    # DFA which matches all binary strings ending in an odd number of '1's
    dfa = DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    if dfa.accepts_input(input_w):
        return {"message": "Accepted"}
    else:
        return {"message": "Rejected"}

