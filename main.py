from fastapi import FastAPI

app = FastAPI()

# TODO: Refactorizar (Crear colecciones para agrupar endpoints)
@app.post("/get_location_by_address")
async def get_location_by_address(address: str):
    # TODO: Obtener latitud y longitud de una dirección
    ...

@app.post("/get_recruitment_trials")
async def get_recruitment_trials(recruiting: bool):
    # TODO: Obtener ensayos que estan abiertos a reclutar o no
    ...

@app.post("/get_trial_age")
async def get_trial_age(method: str, typeof: str):
    # TODO: Obtener promedio, minima o maxima edad de los participantes de una prueba dentro de los dos tipos disponibles (minimo y maximo)
    ...

@app.post("/get_trials_by_year")
async def get_trials_by_year(year: int):
    # TODO: Obtener estudios por año
    ...

@app.post("/get_trials_by_study_type")
async def get_trials_by_study_type(study_type_id: int):
    # TODO: Obtener estudios por tipo de estudio
    ...

@app.post("/get_recruitments_by_gender")
async def get_recruitments_by_gender(gender: str):
    # TODO: Obtener reclutaciones a estudios clinicos filtrados por genero
    ...

@app.post("/get_trials_locations")
async def get_trials_locations(country: str = None):
    # TODO: Obtener ubicaciones: default -> todas, especificas -> por pais
    ...

@app.post("/get_trials_by_phase")
async def get_trials_by_phase(phase: int):
    # TODO: Países que tengas estudios clínicos de tratamientos por fases
    ...

@app.post("/get_trial_contact_on_vaccine")
async def get_trial_contact_on_vaccine(recruiting: bool):
    # TODO: Correo electrónico de centros de investigación que estén realizando ensayos clínicos con vacunas
    ...

@app.post("/get_recruitment_trials")
async def get_recruitment_trials(recruiting: bool):
    # TODO: Página web de resultados de estudios clínicos realizados en cierto país
    ...
