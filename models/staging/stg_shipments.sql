with source as (

    select *
    from {{ ref('shipments') }}

),

renamed as (

    select
        shipment_id,
        supplier_id,
        weight_kg,
        distance_km,
        fuel_type,
        ship_date,
        delivery_delay_days,
        origin_country,
        destination_country
    from source

)

select *
from renamed