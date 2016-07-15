- view: looksandcrosses

  derived_table:
    sql: SELECT * FROM tests.looks_and_crosses
    
  fields:
    - dimension: l
      sql: ${TABLE}.l
      html: |
        <a href="http://localhost:5000/{{ value }}" target="_new"><span style='color:green'>{{ value }}</span></a>
        
    - dimension: m
      sql: ${TABLE}.m
      html: |
        <a href="http://localhost:5000/{{ value }}" target="_new"><span style='color:green'>{{ value }}</span></a>
        
    - dimension: r
      sql: ${TABLE}.r
      html: |
        <a href="http://localhost:5000/{{ value }}" target="_new"><span style='color:green'>{{ value }}</span></a>
        
    - dimension: r_id
      sql: ${TABLE}.r_id
      
  sets:
  
    detail: 
      - l
      - r
      - m 
      - r_id
