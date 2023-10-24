#include "hash_tables.h"

/**
 * hash_table_create - creates an empty has table
 * @size: size of hash table
 * Return: pointer to hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	
	hash_table_t hash_table = malloc(sizeof(hash_table_t * size));

