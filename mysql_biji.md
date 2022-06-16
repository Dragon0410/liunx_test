
# MySQL 引擎有 Innodb, MyISAM, Memory, Merge
    1、Innodb 支持事务，事务安全。提供行级所与外键约束，有缓冲池，用于缓冲数据和索引。用于执行大量的insert， update操作的表；
    2、MySIAM 不支持事务，不支持外键约束、行级锁，操作时需要锁定整张表，不过会保存表的行数。适用于有大量的select操作的表；

# MySQL 事务
    只有使用 innodb 数据库引擎的数据库或表才支持事务
    事务处理用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行
    事务用来管理 insert, update, delete 语句
    必须满足 4 个条件(ACID)：原子性(Atomicity)，一致性(Consistency)，隔离性(Isolation)，持久性(Durability)
        1、原子性：一个事务(transaction)中的所有操作，要么全部完成，要么全部不完成。事务在执行过程中发生错误，回被回滚(Rollback)到事务开始前的状态。
        2、一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。
        3、隔离性：数据了允许多个并发事务，同事对其数据进行读写和修改的能力，隔离性防止多个事务并发执行由于交叉执行而导致数据的不一致。
        4、持久性：事务处理结束后，对数据的修改是永久的，即便系统故障也不会丢失。
    
    事务控制语句
        BEGIN 或者 START TRANSACTION 显示地开启一个事务;
        COMMIT 也可以使用 COMMIT WORK。COMMIT 会提交事务，并使已对数据库进行的所以修改成为永久性的；
        ROLLBACK, 回滚会结束用户的事务，并撤销正在进行的所有未提交的修改；
        SAVEPOINT identifier， SAVEPOINT 允许在事务中创建一个保存点，一个事务中可以有多个 SAVEPOINT;
        ROLLBACK to identifier 把事务回滚到标记点；
        SET TRANSACTION 用来设置事务的隔离级别。MySQL提供的隔离级别有：读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）.
    
    MySQL 事务处理只要有两种方法：
        1、用 BEGIN，ROLBACK，COMMIT 来实现
            begin       开始一个事务
            rollback    事务回滚
            commit      事务确认提交
        2、直接用 SET 来改变 MySQL 的自动提交模式
            set autocommit=0    # 禁止自动提交
            set autocommit=1    # 开启自动提交