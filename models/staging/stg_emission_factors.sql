with source as (

    select *
    from {{ ref('emission_factors') }}

),

renamed as (

    select
        FUEL_TYPE as fuel_type,
        GRAMS_CO2_PER_KM as grams_co2_per_km
    from source

)

select *
from renamed