with source as (

    select *
    from {{ ref('suppliers') }}

),

renamed as (

    select
        supplier_id,
        supplier_name,
        supplier_country,
        sustainability_rating
    from source

)

select *
from renamed