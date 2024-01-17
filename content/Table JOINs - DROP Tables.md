
# Table JOINs - DROP Tables

Video Embed

## DROP Tables

The `DROP` command in SQL is used to remove objects from the database. It's a powerful command that can permanently delete tables, databases, views, or indexes. For the time being, we're just interested in using it to remove tables.

```sql
DROP TABLE tableName; -- Where tableName is the name of the table you want to drop
```

The `DROP` command is typically used during database cleanup, restructuring, or when you need to remove test tables or obsolete database objects. It's part of the standard housekeeping tasks a database engineer or administrator might perform.

A few important things to keep in mind when using `DROP`:
- **Irreversible**: The `DROP` command is irreversible, meaning once you execute it, you can't undo the operation or recover the dropped data unless you have a backup.
- **Use with Caution**: Given its permanent nature, it should be used with caution. Always ensure you have a backup or are absolutely certain you no longer need the data you're removing.
- **Permissions**: You need appropriate permissions to execute a `DROP` command on database objects. You have these permission on your databases but in the real world you may not.



Back: [[Table JOINs - Introduction]] | Next: [[Table JOINs - Magic Store Database]]
