import hashlib, json

def svt(N,c):
    with open(N, 'w', encoding='utf8') as f:
        f.write(json.dumps(c))
    
def ldt(N):
    with open(N, "r", encoding='utf8') as f:
        c = f.read()
    return json.loads(c)
    
def hashme(STR):
    STR = str(STR)
    return str(hashlib.md5(STR.encode('utf-8')).hexdigest())

functionsT35 = [
        {
        "name": "get_risks",
        "description": "You are a world-wide risk expert examining at how to mitigate contagious diseases propagation in the built environment, at all scales. If the user asks for a risk assessment, return a series of risks that exist in the text, focusing on the ones related to contagious diseases.",
        "parameters": {
            "type": "object",
            "properties": {
                "risks": {
                    "type": 'array',
                    "items": {
                        "type": 'object',
                        "description": "A risk, as detailed in the text.",
                        "properties": {
                            "Description" :{
                                "type": 'string', 
                                "description": 'contains the detailed description of risk (up to 25 words).'
                            },
                            "Impact" :{
                                "type": 'string', 
                                "description": 'contains the description of the impact if the risk is not mitigated or eliminated (up to 25 words)'
                            },
                            "Mitigation" :{
                                "type": 'string', 
                                "description": 'details what can be done to elimate or lower the impact or probability of the risk (up to 25 words)'
                            },
                            "Technologies" :{
                                "type": 'string', 
                                "description": 'details what technology can be used to eliminate or lower the impact or probability of the risk (up to 25 words).'
                            },
                            "People" :{
                                "type": 'string', 
                                "description": "provide a list of who or what group of individuals or stakeholders is at risk (up to 25 words)"
                            },
                            "Owner" :{
                                "type": 'string', 
                                "description": "provide a list of who or what group of individuals or stakeholders can implement the mitigation (up to 25 words)"
                            }
                        },
                        "required": ['Description',"Impact","Mitigation","Technologies","People","Owner"],
                    }
                },
            },
            "required": ["risks"],
        },
    }
]