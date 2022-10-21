select venueid, count(venueid) as events_hosted from event group by venueid order by events_hosted desc limit 5

select date_part('month', starttime) as month, count(eventid) as events_hosted from event group by month order by month asc

select sellerid, sum(commission) as total_com, avg(commission) as avg_com from sales group by sellerid order by total_com desc limit 5

select sellerid, sum(commission) as total_com, avg(commission) as avg_com from sales group by sellerid having sum(commission) > 4000 order by total_com desc

select venueid from event group by venueid having count(venueid) > 60

select * from users left join sales on sales.sellerid = users.userid order by users.userid 

select * from event left join venue on venue.venueid = event.venueid order by event.venueid

select * from sales where sales.buyerid in (select userid from users where state in ('AZ'))

select * from event where event.venueid in (select venueid from venue where venuename like '%Stadium')

select * from event where eventid in (select eventid from sales group by eventid having sum(pricepaid) > 50000)