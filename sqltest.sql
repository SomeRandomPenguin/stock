SELECT * FROM stock.kosdaq;

select 회사명, 업종, 주요제품, 지역 from stock.kosdaq;

select * from stock.kosdaq
where 회사명 = '신성델타테크';

select * from stock.kosdaq
order by 상장일 limit 10;

select * from stock.kosdaq
order by 상장일 desc limit 10;

select 회사명, 종목코드 from stock.kosdaq
where 업종 = '반도체 제조업';

select * from stock.kosdaq
where 주요제품 like '%가전%'
order by 회사명;

select * from stock.kosdaq
where 종목코드 = '446150';