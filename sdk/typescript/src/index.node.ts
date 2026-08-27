import { loadData } from './data/node';
import { createConverter as createCoreConverter } from './core/converter';
import type {
  Converter,
  ConverterOptions,
  ExplainEvent,
  ExplainResult,
  Match,
  LookupResult,
  ConversionDetail,
  Source,
  ZhtwData,
} from './core/types';
export { JsonAdapterError } from './core/json-adapter';

let cachedData: ZhtwData | null = null;
let defaultConverter: Converter | null = null;

function getData(): ZhtwData {
  if (!cachedData) cachedData = loadData();
  return cachedData;
}

function getDefault(): Converter {
  if (!defaultConverter) defaultConverter = createCoreConverter(getData());
  return defaultConverter;
}

export function convert(text: string): string {
  return getDefault().convert(text);
}

export function convertJson(text: string): string {
  return getDefault().convertJson(text);
}

export function check(text: string): Match[] {
  return getDefault().check(text);
}

export function lookup(word: string): LookupResult {
  return getDefault().lookup(word);
}

export function explain(text: string): ExplainResult {
  return getDefault().explain(text);
}

export function createConverter(options: ConverterOptions = {}): Converter {
  return createCoreConverter(getData(), options);
}

export type {
  Converter,
  ConverterOptions,
  Match,
  LookupResult,
  ConversionDetail,
  ExplainEvent,
  ExplainResult,
  Source,
};
