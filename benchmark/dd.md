
# flags

    oflag=FLAG[,FLAG]...’ Access the output file using the flags specified by the FLAG argument(s). (No spaces around any comma(s).)

     Here are the flags.  Not every flag is supported on every operating
     system.

     ‘append’
          Write in append mode, so that even if some other process is
          writing to this file, every ‘dd’ write will append to the
          current contents of the file.  This flag makes sense only for
          output.  If you combine this flag with the ‘of=FILE’ operand,
          you should also specify ‘conv=notrunc’ unless you want the
          output file to be truncated before being appended to.

     ‘cio’
          Use concurrent I/O mode for data.  This mode performs direct
          I/O and drops the POSIX requirement to serialize all I/O to
          the same file.  A file cannot be opened in CIO mode and with a
          standard open at the same time.

     ‘direct’
          Use direct I/O for data, avoiding the buffer cache.  Note that
          the kernel may impose restrictions on read or write buffer
          sizes.  For example, with an ext4 destination file system and
          a Linux-based kernel, using ‘oflag=direct’ will cause writes
          to fail with ‘EINVAL’ if the output buffer size is not a
          multiple of 512.

     ‘directory’

          Fail unless the file is a directory.  Most operating systems
          do not allow I/O to a directory, so this flag has limited
          utility.

     ‘dsync’
          Use synchronized I/O for data.  For the output file, this
          forces a physical write of output data on each write.  For the
          input file, this flag can matter when reading from a remote
          file that has been written to synchronously by some other
          process.  Metadata (e.g., last-access and last-modified time)
          is not necessarily synchronized.

     ‘sync’
          Use synchronized I/O for both data and metadata.

     ‘nocache’
          Request to discard the system data cache for a file.  When
          count=0 all cached data for the file is specified, otherwise
          the cache is dropped for the processed portion of the file.
          Also when count=0, failure to discard the cache is diagnosed
          and reflected in the exit status.

          Note data that is not already persisted to storage will not be
          discarded from cache, so note the use of the “sync” options in
          the examples below, which are used to maximize the
          effectiveness of the ‘nocache’ flag.

          Here are some usage examples:

               # Advise to drop cache for whole file
               dd if=ifile iflag=nocache count=0

               # Ensure drop cache for the whole file
               dd of=ofile oflag=nocache conv=notrunc,fdatasync count=0

               # Advise to drop cache for part of file
               # Note the kernel will only consider complete and
               # already persisted pages.
               dd if=ifile iflag=nocache skip=10 count=10 of=/dev/null

               # Stream data using just the read-ahead cache.
               # See also the ‘direct’ flag.
               dd if=ifile of=ofile iflag=nocache oflag=nocache,sync

     ‘nonblock’
          Use non-blocking I/O.

     ‘noatime’
          Do not update the file’s access timestamp.  *Note File
          timestamps::.  Some older file systems silently ignore this
          flag, so it is a good idea to test it on your files before
          relying on it.

     ‘noctty’
          Do not assign the file to be a controlling terminal for ‘dd’.
          This has no effect when the file is not a terminal.  On many
          hosts (e.g., GNU/Linux hosts), this option has no effect at
          all.

     ‘nofollow’
          Do not follow symbolic links.

     ‘nolinks’
          Fail if the file has multiple hard links.

     ‘binary’
          Use binary I/O.  This option has an effect only on nonstandard
          platforms that distinguish binary from text I/O.

     ‘text’
          Use text I/O.  Like ‘binary’, this option has no effect on
          standard platforms.

     ‘fullblock’
          Accumulate full blocks from input.  The ‘read’ system call may
          return early if a full block is not available.  When that
          happens, continue calling ‘read’ to fill the remainder of the
          block.  This flag can be used only with ‘iflag’.  This flag is
          useful with pipes for example as they may return short reads.
          In that case, this flag is needed to ensure that a ‘count=’
          argument is interpreted as a block count rather than a count
          of read operations.

     ‘count_bytes’
          Interpret the ‘count=’ operand as a byte count, rather than a
          block count, which allows specifying a length that is not a
          multiple of the I/O block size.  This flag can be used only
          with ‘iflag’.

     ‘skip_bytes’
          Interpret the ‘skip=’ operand as a byte count, rather than a
          block count, which allows specifying an offset that is not a
          multiple of the I/O block size.  This flag can be used only
          with ‘iflag’.

     ‘seek_bytes’
          Interpret the ‘seek=’ operand as a byte count, rather than a
          block count, which allows specifying an offset that is not a
          multiple of the I/O block size.  This flag can be used only
          with ‘oflag’.

     These flags are not supported on all systems, and ‘dd’ rejects
     attempts to use them when they are not supported.  When reading
     from standard input or writing to standard output, the ‘nofollow’
     and ‘noctty’ flags should not be specified, and the other flags
     (e.g., ‘nonblock’) can affect how other processes behave with the
     affected file descriptors, even after ‘dd’ exits.

# drop_caches

Writing to this will cause the kernel to drop clean caches, as well as
reclaimable slab objects like dentries and inodes.  Once dropped, their
memory becomes free.

To free pagecache:
    echo 1 > /proc/sys/vm/drop_caches
To free reclaimable slab objects (includes dentries and inodes):
    echo 2 > /proc/sys/vm/drop_caches
To free slab objects and pagecache:
    echo 3 > /proc/sys/vm/drop_caches

This is a non-destructive operation and will not free any dirty objects.
To increase the number of objects freed by this operation, the user may run
`sync' prior to writing to /proc/sys/vm/drop_caches.  This will minimize the
number of dirty objects on the system and create more candidates to be
dropped.

This file is not a means to control the growth of the various kernel caches
(inodes, dentries, pagecache, etc...)  These objects are automatically
reclaimed by the kernel when memory is needed elsewhere on the system.

Use of this file can cause performance problems.  Since it discards cached
objects, it may cost a significant amount of I/O and CPU to recreate the
dropped objects, especially if they were under heavy use.  Because of this,
use outside of a testing or debugging environment is not recommended.

You may see informational messages in your kernel log when this file is
used:

    cat (1234): drop_caches: 3

These are informational only.  They do not mean that anything is wrong
with your system.  To disable them, echo 4 (bit 3) into drop_caches.

# good to know

It isn't sticky - you just write to the file to make it drop the caches and then it immediately starts caching again.

Basically when you write to that file you aren't really changing a setting, you are issuing a command to the kernel. The kernel acts on that command (by dropping the caches) then carries on as before.


1. Clear PageCache only.
```bash
# sync; echo 1 > /proc/sys/vm/drop_caches
```
2. Clear dentries and inodes.
```bash
# sync; echo 2 > /proc/sys/vm/drop_caches
```
3. Clear PageCache, dentries and inodes.
```bash
# sync; echo 3 > /proc/sys/vm/drop_caches 
```