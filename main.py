from fastapi import FastAPI

app = FastAPI()


@app.post("/get_address")
async def get_address(address: str):
    # TODO: search country by adress with geocoder
    ...

@app.post("/get_recruitment_trials")
async def get_recruitment_trials(recruiting: bool):
    # TODO: get recruitment trials with params: recruiting (true), not_recruiting (false)
    ...

@app.post("/get_trial_age")
async def get_trial_age(method: str, typeof: str):
    # TODO: Average, minimum or maximun age of people who participated in the recruitments (two types: minimum and maximum)
    ...

@app.post("/get_trials_by_year")
async def get_trials_by_year(year: int):
    # TODO: Trials by year
    ...

@app.post("/get_trials_by_study_type")
async def get_trials_by_study_type(study_type_id: int):
    # TODO: Trials by study type
    ...

@app.post("/")
async def get_recruitment_trials(recruiting: bool):
    # TODO: Ensayos clínicos que estén reclutando sólo hombres/mujeres
    ...

@app.post("/")
async def get_recruitment_trials(recruiting: bool):
    ...

@app.post("/")
async def get_recruitment_trials(recruiting: bool):
    ...

@app.post("/")
async def get_recruitment_trials(recruiting: bool):
    ...

@app.post("/")
async def get_recruitment_trials(recruiting: bool):
    ...

# TOD: Obtener ubicaciones: default -> todas, especificas -> por pais (requerido al usuario mediante ubicacion)
# TODO: Países que tengas estudios clínicos de tratamientos en fase 4
# TODO: Correo electrónico de centros de investigación que estén realizando ensayos clínicos con vacunas
# TODO: Página web de resultados de estudios clínicos realizados en cierto país