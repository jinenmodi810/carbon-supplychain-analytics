with shipments as (

    select *
    from {{ ref('int_shipments_with_emissions') }}

),

final as (

    select
        supplier_id,
        supplier_name,
        supplier_country,
        sustainability_rating,
        count(distinct shipment_id) as total_shipments,
        sum(total_co2_grams) as total_co2_grams,
        avg(total_co2_grams) as avg_co2_grams
    from shipments
    group by
        supplier_id,
        supplier_name,
        supplier_country,
        sustainability_rating

)

select *
from final